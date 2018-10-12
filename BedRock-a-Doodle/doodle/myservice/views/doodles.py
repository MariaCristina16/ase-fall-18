from flakon import JsonBlueprint
from flask import request, jsonify, abort
from myservice.classes.poll import Poll, NonExistingOptionException, UserAlreadyVotedException

doodles = JsonBlueprint('doodles', __name__)

_ACTIVEPOLLS = {} # DICT of created polls
_POLLNUMBER = 0 # index of the last created poll


@doodles.route('/doodles', methods = ['POST', 'GET'])
def all_polls():

    if request.method == 'POST':
        result = create_doodle(request)

    elif request.method == 'GET':
        result = get_all_doodles(request)

    return result


@doodles.route('/doodles/<id>', methods = ['GET', 'DELETE', 'PUT'])
def single_poll(id):
    global _ACTIVEPOLLS
    result = ""

    id = int(id)

    exist_poll(id) # check if the Doodle is an existing one

    if request.method == 'GET': # retrieve a poll
        result = jsonify(_ACTIVEPOLLS[id].serialize())
    elif request.method == 'DELETE':
        result = jsonify({'winners' : _ACTIVEPOLLS[id].get_winners()})
        del _ACTIVEPOLLS[id]
    elif request.method == 'PUT':
        result = vote(id, request)

    return result


@doodles.route('/doodles/<id>/<person>', methods = ['GET', 'DELETE'])
def person_poll(id, person):

    id = int(id)
    exist_poll(id)  # check if the Doodle is an existing one

    if request.method == 'GET':
        result = jsonify({'votedoptions': _ACTIVEPOLLS[id].get_voted_options(person)})
    if request.method == 'DELETE':
        result = jsonify({'removed': _ACTIVEPOLLS[id].delete_voted_options(person)})
    return result


def vote(id, request):
    result = ""
    #TO DO: extract person and option fields from the JSON request
    person = request.json['person']  # person that want to vote
    option = request.json['option']  # option choice of the person
    try:
        result = jsonify({'winners' : _ACTIVEPOLLS[id].vote(person, option)})
    except UserAlreadyVotedException:
        abort(400) # Bad Request
    except NonExistingOptionException:
         abort(400) #Bad Request as UserAlreadyVotedException
    return result


def create_doodle(request):
    global _ACTIVEPOLLS, _POLLNUMBER
    #Increment the _POLLNUMBER identifier
    _POLLNUMBER = _POLLNUMBER + 1

    # Extract title and options fields from the JSON request
    title = request.json['title']  # poll's title
    options = request.json['options']

    # Definition of a new Poll, the parameters are the id,title and options
    poll = Poll(_POLLNUMBER,title,options)

    # Updating the list of the polls
    _ACTIVEPOLLS[_POLLNUMBER] = poll

    return jsonify({'pollnumber': _POLLNUMBER})


def get_all_doodles(request):
    global _ACTIVEPOLLS
    return jsonify(activepolls = [e.serialize() for e in _ACTIVEPOLLS.values()])


def exist_poll(id):
    if int(id) > _POLLNUMBER:
        abort(404) # error 404: Not Found, i.e. wrong URL, resource does not exist
    elif not(id in _ACTIVEPOLLS):
        abort(410) # error 410: Gone, i.e. it existed but it's not there anymore