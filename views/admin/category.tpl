<!--views/admin/category.tpl-->
<link rel="stylesheet" href="/static/styles/admin/category.css" />

<form action="/admin/category" method="post">
    %if 'item' in data:
    <input type="text" value="{{data['item']['title']}}" name="title" 
    required placeholder="ឈ្មោះ​ជំពូក" />
    <input type="text" value="{{data['item']['thumb']}}" name="thumb" 
    required placeholder="តំណរភ្ជាប់​រូប​សញ្ញា" />
    <input type="datetime-local" value="{{data['item']['date']}}" name="datetime" required />
    <input type="submit" value="បញ្ជូន" />
    %else:
    <input type="text" name="title" required placeholder="ឈ្មោះ​ជំពូក" />
    <input type="text" name="thumb" required placeholder="តំណរភ្ជាប់​រូប​សញ្ញា" />
    <input type="datetime-local" name="datetime" required />
    <input type="submit" value="បញ្ជូន" />
    %end
</form>