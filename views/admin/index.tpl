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
</section>