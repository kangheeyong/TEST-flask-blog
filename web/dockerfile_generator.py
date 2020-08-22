if __name__ == "__main__":
    dockerfile = '''FROM python:3.8

RUN apt-get update
RUN apt-get install redis-tools -y

RUN pip install --upgrade pip
'''
    for l in open('requirements.txt'):
        l = l.strip()
        if not l or l.startswith('#'):
            continue
        dockerfile += "RUN pip install {}\n".format(l)

    dockerfile += '''
RUN mkdir -p /app

WORKDIR /app
'''
    with open('Dockerfile', 'w') as file :
        file.write(dockerfile)
