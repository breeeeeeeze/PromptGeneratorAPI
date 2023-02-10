import uvicorn
from config import config


def main():
    uvicorn.run('main:app', port=config.api.port, reload=config.api.reload, log_level='info')


if __name__ == '__main__':
    main()
