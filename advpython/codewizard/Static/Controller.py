import web

urls = (
    '/', 'home',
    '/register', 'register'
)

render = web.template.render("C:\\Users\\neela\desktop\\advpython\\codewizard\\Views\\Templates", base="MainLayout")
app = web.application(urls, globals())


class home:
    def GET(self):
        return render.Home()

class register:
    def GET(self):
        return render.Register()

if __name__ == "__main__":
    app.run()
