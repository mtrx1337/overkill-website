from app import app
import sys

if __name__ == '__main__':
    print_help = lambda : print('main.py <PORT>')
    if len(sys.argv) < 2:
        print_help()
        exit()
    PORT = sys.argv[1]
    app.run(port=PORT)

