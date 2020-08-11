import web

urls = (
    '/(.*)/(.*)', 'Index'
)

render = web.template.render("resources/")
app = web.application(urls, globals())


class Index:
    def GET(self, name, age):
        return render.main(name, age)


if __name__ == "__main__":
    app.run()
