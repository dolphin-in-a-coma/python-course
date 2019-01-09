$(document).ready(function(){
     $(function(){
          $('.edit-friend').click(function(){
               friend = $(this).attr('id').substr($(this).attr('id').indexOf("-")+1);
               $.post('/ajax/edit_friend.php',
                         {friend:friend},
                         function(data){
               });               
               friend_link_text = $(this).html().replace(/^\s\s*/, '').replace(/\s\s*$/, '');
	          if (friend_link_text=="Добавить в друзья")
	          {
	               $(this).html("Удалить из друзей");
	          }
	          else
	          {
	               $(this).html("Добавить в друзья");       
	          }
          });
     });
});