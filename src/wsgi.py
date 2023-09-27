from src import create_application

application = create_application()


if __name__ == "__main__":
    application.run(host='127.0.0.1', debug=True)
