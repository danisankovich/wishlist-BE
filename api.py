import time
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

# get user details. if aggregatedWishlists = true, also collect the wishlists for each valid id
@app.route('/userDetails')
def get_current_user():
    aggregatedWishlists = request.args.get('aggregatedWishlists')
    
    userFile = open('./mock/user.json', 'r')
    userData = json.loads(userFile.read())
    userFile.close()

    if aggregatedWishlists:
        wishlistIds = userData['wishlistIds']
        wishlistFile = open('./mock/wishlists.json', 'r')
        wishlistData = json.loads(wishlistFile.read())
        wishlistFile.close()
        filtered = filter(lambda w: w['id'] in wishlistIds, wishlistData)
        userData['wishlists'] = list(filtered)
    return userData


@app.route('/wishlists')
def getWishlists():
    f = open('./mock/wishlists.json', 'r')
    data = json.loads(f.read())
    f.close()
    return data

@app.route('/wishlist')
def getWishlistById():
    wishlistId = request.args.get('wishlistId')
    f = open('./mock/wishlists.json', 'r')
    data = json.loads(f.read())
    f.close()
    wishlist = next(filter(lambda v: v['id'] == wishlistId, data), None)

    return wishlist
