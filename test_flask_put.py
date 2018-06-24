from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

d = {}

class TodoSimple(Resource):
	def get(self):
		return {"response":"Hi"};

	def put(self):
		question = request.form['data'].lower()
		if(question == "hi"):
			return {"response":"Hi"};
		elif(question == "help me know python"):
			return {"response":"Do you mean programming or snake?"};
		elif(question == "snake"):
			return {"response":"Pythons are a family of nonvenomous snakes found in Africa, Asia, and Australia. \nAmong its members are some of the largest snakes in the world. \nhttps://en.wikipedia.org/wiki/Pythonidae"};
		elif(question == "programming"):
			return {"response":"What's your experience level?\nBeginner?\nIntermediate?\nAdvanced?"};
		elif(question == "beginner"):
			return {"response":"How do you show \"Hello World!\"?"};
		elif(question == "print(\"hello world!\")"):
			return {"response":"Congrats! Correct!"};
		elif(question == "print(\"hello world!)"):
			return {"response":"Almost correct. Try again?"};
		return {"response":"Hi"};

api.add_resource(TodoSimple, '/')


if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run()