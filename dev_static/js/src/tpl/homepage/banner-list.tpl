<% _.each(list, function(banner, idx) { %>
<tr data-banner-id="<%= banner.id %>">
	<td><%= banner.name %></td>
	<td><a class="preview-link" href="javascript:;" data-image-url="<%= banner.original %>"><%= banner.name %>(大图)</a></td>
	<td><a class="preview-link" href="javascript:;" data-image-url="<%= banner.thumbnail %>"><%= banner.name %>(缩略图)</a></td>
	<td><%= banner.background %></td>
	<td><%= banner.background_image_width %></td>
	<td><%= banner.background_image_color %></td>
	<td><a href="<%= banner.page_url %>" target="_blank"><%= banner.name %></a></td>
	<td><input class="order-input" type="text" data-banner-id="<%= banner.id %>"  value="<%= banner.order %>" maxlength="2"/></td>
	<td><%= banner.created_time %></td>
	<td><%= banner.modified_time %></td>
	<td><%= banner.update_user %></td>
	<td><span class="hide-status"><%= banner.is_active=="1"  ? '是' : '否' %></span></td>
	<td>
		<a class="edit-link" href="javascript:;" data-banner-id="<%= banner.id %>">编辑</a>
		<a class="toggle-status-link" href="javascript:;" data-banner-id="<%= banner.id %>" data-active-status="<%= banner.is_active %>"><%= banner.is_active=="1"  ? '隐藏' : '显示' %></a>
	</td>
</tr>
<% }); %>
