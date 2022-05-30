<!--views/admin/index.tpl-->
<link href="/static/styles/admin/index.css" rel="stylesheet" />
 
<section class='Index'>
    <div class="header-wrapper">
    <header class='region'>
        <div class='logo'>{{ data['pageTitle'] }}</div>
 
        <form action='/admin/search' method='post'>
            <select name="select">
                <option>ការផ្សាយ</option>
                <option>ជំពូក</option>
                <option>សៀវភៅ</option>
                <option>អ្នក​ប្រើប្រាស់</option>
            </select>
            <input type='text' name="q" placeholder="Search" required />
            <input type="submit" value='បញ្ជូន'​ />
        </form>
 
        <div class='logout'><a href='/'>ទំព័រ​មុខ</a> | <a href='/login/logout'>ចេញ​ក្រៅ</a></div>
    </header>
    </div>

    <div class="main region">
        <div class="sidebar">
            <div class="menu">
                <a href="/admin/post"><img src="/static/images/movie.png" /></a>
                <a href="/admin/post">ការផ្សាយ</a>  

                <a href="/admin/category"><img src="/static/images/category.png" /></a>
                <a href="/admin/category">ជំពូក</a>

                <a href="/admin/upload"><img src="/static/images/upload.png" /></a>
                <a href="/admin/upload">Upload</a>

                <a href="/admin/user"><img src="/static/images/users.png" /></a>
                <a href="/admin/user">អ្នក​ប្រើប្រាស់</a>

                <a href="/admin/setting"><img src="/static/images/setting.png" /></a>
                <a href="/admin/setting">Setting</a>
            </div>
        </div>
        <div class="content">
            <%
            if '/post' in data['route']:
                include('admin/post.tpl')
            elif '/category' in data['route']:
                include('admin/category.tpl')
            end
            %>
        </div>
    </div>

    <div class="Listing region">
        %if 'items' in data:
        <ul class="list">
            %for item in data['items']:
            <li class="item">
                <a class="thumb" href="/{{data['type']}}/{{item['id']}}">
                    <img src="{{item['thumb']}}" />
                </a>
                <div>
                    <a class="title" href="/{{data['type']}}/{{item['id']}}">
                        {{item['title']}}
                    </a>
                    <span id="{{item['id']}}">
                        <script>
                            var date = (new Date('{{item["date"]}}')).toLocaleDateString()
                            $('.Listing .list .item #{{item["id"]}}').append(date)
                        </script>
                    </span>
                </div>
                <div class="edit">
                    <a href="/admin/{{data['type']}}/edit/{{item['id']}}">
                        <img src="/static/images/edit.png" />
                    </a>
                    <a href="/admin/{{data['type']}}/delete/{{item['id']}}">
                        <img src="/static/images/delete.png" />
                    </a>
                </div>
            </li>
            %end
        </ul>
        %end
        <div class="paginate region">
            <img onclick="paginate(`{{data['route']}}`)" src="/static/images/load-more.png"/>
        </div>
    </div>

</section>