# 7420-Assessment

Assessment2 Deployment:
API: http://52.62.138.189:8000/api/citys/
React frontend: http://transfergoods-frontend.s3-website-ap-southeast-2.amazonaws.com/

What transfergoods do?  

C2C platform provides the Postal services by individual, which committed to solving fast, small personal international and domestic express delivery needs.  

It provides general functions such as sign up, sign in, find lost password (through email), log out and change password.  

As it is a C2C platform, its main function allows users to create their own services and needs orders. Meanwhile, Users can also place services and needs orders when they need them. Thus, there are "My order" and "My publish" tabs to helps users find, track, edit and delete items.  

In purpose of allowing buyer and seller could communicate with each other, there is Message function. When user is interesting of one item, he can talk to item's owner directly. And the item's owner could find inbox message in "Inbox" tab and feedback the message, while user could track sent message in "Outbox" tab.  
   
HOST: http://transfergoods.co.nz/   http://www.transfergoods.co.nz/   https://transfergoods.herokuapp.com/

How server-side rendering works?
  Server-side rendering (SSR), is the ability of an application to contribute by displaying the web-page on the server instead of rendering it in the browser. Server-side sends a fully rendered page to the client; the client’s JavaScript bundle takes over and allows the SPA framework to operate. There is also client-side rendering which slows down the procedure of viewing and interacting with the web page.
  In Django:
  `def index(request):
    orderstatus = OrderStatus.objects.get(status_name='published')
    allneeds = Need.objects.filter(orderstatus=orderstatus, isDeleteByUser=False)
    return render(request, 'index.html', context={'allneeds': allneeds})`
  Define function, register router in url.py. Collecting model data by Model.objects.filter. Through return render() function, pass data to html file. 
  
ERD:
  ![image info](./staticfiles/ERD.jpg)
  
 
