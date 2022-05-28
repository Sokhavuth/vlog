<!--views/base.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{ data['siteTitle'] }}/{{data['pageTitle']}}</title>
    <script src="/static/scripts/jquery.js"></script>
    <link href="/static/images/siteLogo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
    <link href="/static/styles/base.css" rel="stylesheet"></link>
  </head>
  <body>
  <%
    if(data['route'] == '/login'):
        include('login.tpl')
    elif('/admin/' in data['route']):
        include('admin/index.tpl')
    end
  %>
  </body>
</html>