<!--views/admin/category.tpl-->
<link rel="stylesheet" href="/static/styles/admin/category.css" />

<form action="/admin/category" method="post">
    <input type="text" name="title" required placeholder="ឈ្មោះ​ជំពូក" />
    <input type="text" name="thumb" required placeholder="តំណរភ្ជាប់​រូប​សញ្ញា" />
    <input type="datetime-local" name="datetime" required />
    <input type="submit" value="បញ្ជូន" />
</form>