from golf import create_app
#Main executable file that pulls from the entire golf package to run the code

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


