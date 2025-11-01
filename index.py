import tornado.web as tw
import tornado.ioloop as ti

class basicRequestHandler(tw.RequestHandler):
    def get(self):
        self.write("Hellow world, This is a Python Command")

class listRequestHandler(tw.RequestHandler):
    def get(self):
        self.render("index.html")

class evenquery(tw.RequestHandler):
    def get(self):
        num=self.get_argument("num")
        if(num.isdigit()):
            r="odd" if int(num)%2 else "even"
            self.write(f"The int {num} is {r}")
        else:
            self.write(f"{num} is not valid integer")

class resourceParams(tw.RequestHandler):
    def get(self,studentName,courseId):
        self.write(f"Welcome {studentName} the course is {courseId}")


if __name__=="__main__":
    app= tw.Application(
        [
            (r"/",basicRequestHandler),
            (r"/animal", listRequestHandler),
            (r"/isEven", evenquery),
            (r"/students/([a-z]+)/([0-9]+)",resourceParams)
            ]
    )
    port= 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")

    ti.IOLoop.current().start()