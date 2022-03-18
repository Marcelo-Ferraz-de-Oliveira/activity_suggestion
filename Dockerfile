#Build container with frontend and backend together, running with gunicorn server

#Build the React frontent
FROM node:16-alpine as build
WORKDIR /activity_suggestions/react_frontend
ENV PATH /react_frontend/node_modules/.bin:$PATH
COPY ./react_frontend/package.json  ./
COPY ./react_frontend/src ./src
COPY ./react_frontend/public ./public
RUN npm install
RUN npm run build

#Build the Python backend and copy frontend build static files to run togherer in gunicorn
FROM python:3.9
#Get Openweather API_KEY from --build-arg
ARG API_KEY
ENV ENV_API_KEY=${API_KEY} 
WORKDIR /activity_suggestions
COPY --from=build /activity_suggestions/react_frontend/build ./react_frontend/build
COPY ./activity_suggestions ./activity_suggestions
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
RUN touch ./activity_suggestions/api_key.py
RUN echo API_KEY = \"${ENV_API_KEY}\" > ./activity_suggestions/api_key.py
ENV FLASK_ENV production

#Run gunicorn
EXPOSE 3000
ENV PORT 3000
WORKDIR /activity_suggestions
CMD gunicorn --bind=0.0.0.0:$PORT activity_suggestions.app:app
