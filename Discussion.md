Architecture:
- When would you prefer to develop an Assignment 1 style web application (Server-side rendering, serving HTML)?
A: By now, I feel serverside rendering is enough for the app needs. But the other existed online app are rich of UX design, which is good for end users' experience. And almost all the potential employers are looking for front-end and back-end developer separately. So, building API and handle the front-end framework are some must skills we need. In the mean time, serverside rendering is a fast way to build easy app.
- When would you prefer an Assignment 2 one (REST API & Single Page Application)?
A: When there is need for a big amount of js content in front-end.

Version Control:
- What is git and what is it used for?
A: GIT is kind of language to look after file content change history, which is used to help track the version of the app.
- List 3 git commands you’ve learned in this course.
A: git init; git commit; git push; git add <file>; git add remote;
- What is GitHub and what is it used for?
A: GitHub is the biggest online platform for store git files and manage multiple party work for personal and organizations.
- What is Kanban and what is it used for?
A: Kanban boards offer a way to visually manage your work.
- What is Markdown and what is it used for?
A: Markdown is a lightweight markup language with plain-text-formatting syntax.

Platform vs Infrastructure:
- What are some of the pros and cons of using Platform-as-a-Service (PaaS) providers such as Heroku?
A: Pros: easy to config; Cons: high costs and potential secirity issues;
- What are some of the pros and cons of using Infrastructure-as-a-Service providers such as Amazon?
A: Pros: The most widely used in the industry; Cons: May suffer 'all the eggs in one basket' risk.

Web Frameworks:
- What is Django? What are some of its useful features?
A: Django is a popular web development framework based on Python; Django encourages rapid development and clean, pragmatic design.
- What is a model?
A: A model is a object with many attributes, which is used to define a table in a database.
- What is a view?
A: In Django, view is somewhere to define the function for handle data and give response; In other MVC, it names controllor.
- Name two other popular non-Python web frameworks.
A: ASP.Net Core based on C#; Spring based on JAVA.
- What is WSGI? What is ASGI?
A: WSGI is the Web Server Gateway Interface, which is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request; ASGI means the Asynchronous Server Gateway Interface, which is the specification which Channels and Daphne are built upon, designed to untie Channels apps from a specific application server and provide a common way to write application and middleware code.
- What is celery and what are task queues used for?
A: Celery is a Python Task-Queue system that handle distribution of tasks on workers across threads or network nodes; Task Queue is defined as a mechanism to synchronously distribute a sequence of tasks among parallel threads of execution.

Databases:
- What is PostgreSQL? Using StackShare, list 3 well-known companies that use PostgreSQL.
A: PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance; Uber, Netflix and Instagram.
- List two other well-known databases.
MySql; MS SQL.
- What are some of the pros and cons of using an Object Relational Mapper (ORM)?
A: Pros: ORMs will shield your application from SQL injection attacks since the framework will filter the data; Cons: slower than others.
- What is the purpose of database migrations?
A: Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into the database schema.
- What is redis and what are two things it can be used for?
A: Redis is an in-memory data structure project implementing a distributed, in-memory key–value database with optional durability; It can be used as database, cache and message broker.
- Why do we use caches?
A: Improve response speed. eg. end users do not need to wait the browser download the same images from the networks when access the previous page.

HTTP & REST:
- Which four HTTP methods does REST use for performing CRUD operations?
A: GET; POST; PUT; DELETE;
- What is Django REST Framework used for?
A: Help build restful API from Django backend.
- What is serialization and why do we use it?
A: The serializer consists of a series of serialized fields. The function of the serialized field is to convert the Python data type to the original data type (usually a character type or a binary type) when serializing resources. Pass between the server and the browser; when deserializing, convert the original data type to a Python data type. During the conversion process, the legality of the data is also checked.
- Which type of object serialization notation is most commonly used on the web?
A: ModelSerializer
- What is Postman and what is it used for?
A: Postman is a great tool when trying to dissect RESTful APIs made by others or test ones you have made yourself. It offers a sleek user interface with which to make HTML requests, without the hassle of writing a bunch of code just to test an API's functionality.
- What are websockets and what are they used for?
A: The WebSocket protocol enables interaction between a web browser (or other client application) and a web server with lower overhead than half-duplex alternatives such as HTTP polling, facilitating real-time data transfer from and to the server.

Javascript:
- What is NodeJS and how is it different from in-browser Javascript?
A: Node.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine; JavaScript is a simple programming language which runs in any browser JavaScript Engine. Whereas Node JS is an interpreter or running environment for a JavaScript programming language which holds a lot of excesses require libraries which can easily be accessed from JavaScript programming for better use.
- What is npm and what is it used for?
A: npm is a package manager for the JavaScript programming language. It is the default package manager for the JavaScript runtime environment Node.js. It consists of a command line client, also called npm, and an online database of public and paid-for private packages, called the npm registry.
- What is ES6? List the names of 3 features that ES6 provides.
A: ES6 refers to version 6 of the ECMA Script programming language. ECMAScript is a general-purpose programming language, standardized by Ecma International according to the document ECMA-262. It was inspired by JavaScript and JScript and was created to help foster multiple independent implementations. Constants, Scoping and Arrow Functions.
- What is ReactJS and what is it used for?
A: React is an open-source JavaScript library for building user interfaces.
- List two popular alternative Javascript libraries to ReactJS.
A: VUE Angular
- What is the DOM? What is a virtual DOM?
A: The Document Object Model (DOM) is a programming API for HTML and XML documents. It defines the logical structure of documents and the way a document is accessed and manipulated; The virtual DOM (VDOM) is a programming concept where an ideal, or “virtual”, representation of a UI is kept in memory and synced with the “real” DOM by a library such as ReactDOM.
- What is the difference between sessionStorage and localStorage?
A: Local storage and Session storage are the web srorage objects. Session storage is destroyed once the user closes the browser whereas, Local storage stores data with no expiration date. The sessionStorage object is equal to the localStorage object, except that it stores the data for only one session.
- What is a library like Material-UI used for?
A: React components for faster and easier web development.

Docker:
- Why do we run apt-get update && apt-get install -y in one command when using Docker?
A: In most Linux distributions, packages rotate in versions all the time, but the listing of these indexes that tell us where to find these is baked into the original Docker image when it gets created. Before we can install a package, in most cases our index files have been stale for too long, so we need to update them.
- What are Docker containers and what are the pros and cons of using them?
A: Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package; Containers don't run at bare-metal speeds.The container ecosystem is fractured. Persistent data storage is complicated. 
- What is the difference between ADD and COPY with Docker?
A: COPY takes in a src and destination. It only lets you copy in a local file or directory from your host (the machine building the Docker image) into the Docker image itself. ADD lets you do that too, but it also supports 2 other sources
- What is a .dockerignore file used for?
A: dockerignore file is similar to gitignore file, used by the git tool. It allows you to specify a pattern for files and folders that should be ignored by the Docker client when generating a build context.
- What is Kubernetes and why didn’t we use it?
A: Kubernetes is an open-source container-orchestration system for automating application deployment, scaling, and management.

Deployment:
- What is Amazon S3 used for?
A: Amazon S3 is a service offered by Amazon Web Services that provides object storage through a web service interface. 
- What is Amazon ECS?
A: Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service.
- What is the difference between ECS Fargate and EC2?
A: ECS has two launch types that can define how the compute resources will be managed. The traditional EC2 launch type detailed in the overview above utilizes your own EC2 instances. Fargate removes the responsibility of provisioning, configuring and managing the EC2 instances by allowing AWS to manage the EC2 instances.
- Name 3 other cloud providers.
A: IBM, Azure, Alibaba Cloud
- What is Sentry and what is it used for?
A: Sentry empowers developers to quickly triage and resolve issues while reducing everything-is-on-fire stress, chaos, and potential financial loss, by providing cross-stack visibility and deep context about errors.
- What is Cloudflare and what is it used for?
A: CloudFlare is a network of data centers that sits between your web server and the rest of the internet.
- What is SendGrid and what is it used for?
A: SendGrid is a Denver, Colorado-based customer communication platform for transactional and marketing email. 
- What is the difference between a DNS A record and a CNAME record?
A: The A record maps a name to one or more IP addresses when the IP are known and stable. The CNAME record maps a name to another name. It should only be used when there are no other records on that name. 

Meta:
- What are some of the mistakes or difficulties you encountered in developing these 2 assignments?
A: The most mistakes and time were taken by the deployment part, which takes lots of efforts to learn for the first time you use them.
- What have you learned from this course that you think might be useful in your career?
A: This course is a great help for those who want to become full-stack web developers. Help me not only understand the top web technologies, but also use them to complete some real projects. So I feel very fortunate to learn this course, and I recommend it to others.
