from gutenberg import *;
from test import *;

# @Test
# def testError():
#     when(Method.POST, "http://localhost:8181/bills", {
#         "clientId": 0,
#         "creationDate": "2017-08-21T16:59:20.142Z",
#         "dueTerm": "IMMEDIATE",
#         "items": [
#             {
#                 "price": 0.00,
#                 "note": "Item note",
#                 "productId": 0,
#                 "quantity": -1
#             }
#         ]
#     }).expect(Status.BAD_REQUEST, {
#         "errors": [
#             {
#                 "error": "not found",
#                 "description": "product 0 not found",
#                 "entity": "product"
#             },
#             {
#                 "error": "invalid quantity",
#                 "description": "product 1 quantity cannot be negative",
#                 "entity": "product"
#             },
#             {
#                 "error": "not found",
#                 "description": "client 0 not found",
#                 "entity": "client"
#             }
#         ]
#     });

# done();

@Case
def someCase():
    @Test
    def testError():
        when(Method.POST, "http://localhost:8181/bills", {
            "clientId": 0,
            "creationDate": "2017-08-21T16:59:20.142Z",
            "dueTerm": "IMMEDIATE",
            "items": [
                {
                    "price": 0.00,
                    "note": "Item note",
                    "productId": 0,
                    "quantity": -1
                }
            ]
        }).expect(Status.BAD_REQUEST, {
            "errors": [
                {
                    "error": "not found",
                    "description": "product 0 not found",
                    "entity": "product"
                },
                {
                    "error": "invalid quantity",
                    "description": "product 1 quantity cannot be negative",
                    "entity": "product"
                },
                {
                    "error": "not found",
                    "description": "client 0 not found",
                    "entity": "client"
                }
            ]
        });

@Case
def someCase():
    @Test
    def testError():
        when(Method.POST, "http://localhost:8181/bills", {
            "clientId": 0,
            "creationDate": "2017-08-21T16:59:20.142Z",
            "dueTerm": "IMMEDIATE",
            "items": [
                {
                    "price": 0.00,
                    "note": "Item note",
                    "productId": 0,
                    "quantity": -1
                }
            ]
        }).expect(Status.BAD_REQUEST, {
            "errors": [
                {
                    "error": "not found",
                    "description": "product 0 not found",
                    "entity": "product"
                },
                {
                    "error": "invalid quantity",
                    "description": "product 1 quantity cannot be negative",
                    "entity": "product"
                },
                {
                    "error": "not found",
                    "description": "client 0 not found",
                    "entity": "client"
                }
            ]
        });
    @Test
    def testNoError():
        when(Method.POST, "http://localhost:8181/bills", {
            "clientId": 0,
            "creationDate": "2017-08-21T16:59:20.142Z",
            "dueTerm": "IMMEDIATE",
            "items": [
                {
                    "price": 0.00,
                    "note": "Item note",
                    "productId": 0,
                    "quantity": -1
                }
            ]
        }).expect(Status.BAD_REQUEST, {
            "errors": [
                {
                    "error": "not found",
                    "description": "product 0 not found",
                    "entity": "product"
                },
                {
                    "error": "invalid quantity",
                    "description": "product 0 quantity cannot be negative",
                    "entity": "product"
                },
                {
                    "error": "not found",
                    "description": "client 0 not found",
                    "entity": "client"
                }
            ]
        });
