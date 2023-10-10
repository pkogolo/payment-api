from flask import jsonify, make_response
import uuid
from dotenv import load_dotenv

load_dotenv()


def generateAnyId(default = 6):
    id = str(uuid.uuid4().int)[:default]
    return id

# e8_value = generateAnyId(8)


def exceptDefault(erroRef):
    statuscode = 412
    status ='precondition_failed'
    return {'message':str(erroRef), 'status':status, 'statusCode':statuscode}

def exceptSpecific(erroRef, statuscode=404, status="failed"):
    return {'message':str(erroRef), 'status':status, 'statusCode':statuscode}


# ex = exceptSpecific(erroRef)

def build_response(status_code, message):
    mesge = {"message":message}
    response = make_response(mesge)
    response.status_code = status_code
    response.headers['Content-Type'] = 'application/json'
    return response
