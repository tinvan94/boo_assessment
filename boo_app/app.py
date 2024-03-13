
from fastapi import FastAPI, Body, Request
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from boo_app.database import profile_collection, account_collection, comment_collection, like_collection, \
    vote_collection, vote_option_collection, vote_option_category_collection
from boo_app.models.account import AccountSchema
from boo_app.models.comment import CommentSchema
from boo_app.models.like import CommentLikeSchema
from boo_app.models.profile import ProfileSchema
from boo_app.models.vote import VoteSchema

app = FastAPI()


@app.get('/healthcheck')
async def healthcheck():
    return {"system": "Boo App"}


# PROFILE
@app.post('/profile')
async def add_profile(profile_data: ProfileSchema = Body(...)):
    prof = jsonable_encoder(profile_data)
    profile = await profile_collection.insert_one(prof)
    new_profile = await profile_collection.find_one({"_id": profile.inserted_id})
    new_profile = {
        "id": str(new_profile["_id"]),
        "name": str(new_profile["name"]),
    }
    return new_profile


@app.get('/profile/{id}')
async def get_profile(id):
    profile = await profile_collection.find_one({"_id": ObjectId(id)})
    if profile:
        profile_data = {
            "id": str(profile["_id"]),
            "name": str(profile["name"]),
        }
        return profile_data
    else:
        return {}


# ACCOUNT
@app.post('/account')
async def add_account(account_data: AccountSchema = Body(...)):
    acc = jsonable_encoder(account_data)
    profile = await account_collection.insert_one(acc)
    new_account = await account_collection.find_one({"_id": profile.inserted_id})
    account_resp = {
        "id": str(new_account["_id"]),
        "name": str(new_account["name"]),
    }
    return account_resp


@app.get('/account/{id}')
async def get_account(id):
    acc = await account_collection.find_one({"_id": ObjectId(id)})
    if acc:
        acc_data = {
            "id": str(acc["_id"]),
            "name": str(acc["name"]),
        }
        return acc_data
    else:
        return {}


# COMMENT
@app.post('/comment')
async def add_comment(comment_data: CommentSchema = Body(...)):
    acc = jsonable_encoder(comment_data)
    comm = await comment_collection.insert_one(acc)
    new_comm = await comment_collection.find_one({"_id": comm.inserted_id})
    comm_resp = {
        "id": str(new_comm["_id"]),
        "title": str(new_comm["title"]),
        "content": str(new_comm["content"]),
    }
    return comm_resp


@app.get('/comments')
async def get_comment(req: Request):

    params = dict(req.query_params)

    # required field
    profile_id = params.get('profile_id')

    sort_by = params.get('soft_by')
    vote_option_category = params.get('vote_option_category')

    cond = {
        "profile_id": profile_id,
    }

    # filter comments by vote option
    if vote_option_category:
        option_category = await vote_option_category_collection.find_one({"name": vote_option_category})
        option = await vote_option_collection.find({"category_id": option_category['_id']})
        votes = await vote_collection.find({"vote_option_id": option['_id']})
        account_ids = [v['account_id'] for v in votes] if votes else [-1]
        cond.update({
            'account_id': {'$in': account_ids}
        })

    # sort by best/recent
    if sort_by == 'recent':
         comms = comment_collection.find(cond).sort(['created_at', -1])
    elif sort_by == 'best':
        pipeline = [
            {
                "$lookup": {
                    "from"        : "likes",
                    "localField"  : "_id",
                    "foreignField": "comment_id",
                    "as"          : "related_docs"
                }
            },
            {
                "$addFields": {
                    "related_docs_count": {"$size": "$related_docs"}
                }
            },
            {
                "$sort": {"related_docs_count": -1}
            }
        ]
        comms = comment_collection.find(cond).aggregate(pipeline)
    else:
        comms = comment_collection.find(cond)

    comm_resp = []
    async for comm in comms:
        comm_resp.append({
            "id": str(comm["_id"]),
            "title": comm["title"],
            "content": comm["content"],
        })
    return comm_resp


@app.get('/comment/count_like/{id}')
async def count_like(id):
    like_count = await like_collection.count_documents({'comment_id': id})
    return {'total_count': like_count}


# LIKE
@app.post('/like')
async def add_like(like_data: CommentLikeSchema = Body(...)):
    like = jsonable_encoder(like_data)
    lik = await like_collection.insert_one(like)
    new_like = await like_collection.find_one({"_id": lik.inserted_id})
    _resp = {
        'is_success': True if new_like else False,
    }
    return _resp


@app.delete('/like/{id}')
async def unlike(id):
    await like_collection.delete_one({"_id": ObjectId(id)})
    return {'is_delete': True}


# VOTE
@app.post('/vote')
async def add_vote(vote_data: VoteSchema = Body(...)):
    vote = jsonable_encoder(vote_data)
    vot = await vote_collection.insert_one(vote)
    new_vote = await vote_collection.find_one({"_id": vot.inserted_id})
    _resp = {
        'is_success': True if new_vote else False,
    }
    return _resp


@app.get('/votes')
async def get_votes(req: Request):

    params = dict(req.query_params)

    # required field
    profile_id = params.get('profile_id')
    account_id = params.get('account_id')
    cond = {
        "profile_id": profile_id,
        "account_id": account_id,
    }

    votes = vote_collection.find(cond)
    comm_resp = []

    async for vote in votes:
        option = await vote_option_collection.find_one({"_id": vote.vote_option_id})
        option_category = await vote_option_category_collection.find_one({"_id": vote.vote_option_id})
        comm_resp.append({
            'id': vote['id'],
            'vote_option': option['name'],
            'vote_option_category': option_category['name']
        })
    return comm_resp
