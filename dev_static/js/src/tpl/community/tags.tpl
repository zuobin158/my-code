<div class="tags-view">
	<h3>标签&nbsp;<a class="edit-link" href="javascript:;"><span class="glyphicon glyphicon-pencil"></span></a></h3>
	<% _.each(list, function(tag, idx) { %>
	<% if(idx%2 == 0){ %><div class="tag-row"><% } %>
	<% if(tag.label != null && tag.label != ""){ %><div class="tag-col"><%= idx+1 + "." + tag.label %></div><% } %>
	<% if(idx%2 == 1){ %></div><% } %>
	<% }); %>
</div>