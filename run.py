from backoffice.interface.apps import create_app




if __name__ == '__main__':
    app = create_app()
    app.run(port=9090)