<div class="tags-view">
	<h3>标签编辑</h3>
	<% _.each(list, function(tag, idx) { %>
	<% if(idx%2 == 0){ %><div class="tag-row"><% } %>
		<div class="tag-label"><%= idx+1 + "." %></div>
		<div class="tag-col"><input type="text" class="form-control input-sm tag-input" value="<%= tag.label %>" data-tag-id="<%= tag.tagId %>"/></div>
	<% if(idx%2 == 1){ %></div><% } %>
	<% }); %>
    <div class="tag-row bottom-row">
        <div class="text-danger hint-block"></div>
    </div>
	<div class="tag-row bottom-row">
		<div class="tag-col"><button type="button" class="btn btn-default save-btn">保存</button></div>
		<div class="tag-col"><button type="button" class="btn btn-default cancel-btn">取消</button></div>
	</div>
</div>
