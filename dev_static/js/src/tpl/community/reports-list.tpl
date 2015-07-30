<% _.each(list, function(report, idx) { %>
<tr data-report-id="<%= report.id %>">
	<td><%= report.reportDate %></td>
	<td><%= report.type %></td>
	<td><%= report.reason %></td>
	<td><%= report.reporter %></td>
	<td><%= report.reported %></td>
	<td><%= report.postId %></td>
	<td><a class="popup-link" href="javascript:;" data-post-id="<%= report.postId %>"><%= report.postTitle %></a></td>
	<td><%= (report.commentId == "") ? "--" : report.commentId %></td>
	<td><%= (report.commentContent == "") ? "--" : report.commentContent %></td>
	<td><span class="action-status"><%= report.status %></span></td>
	<td class="action-node">
		<% if(report.status == "未处理"){ %>
		<a class="action-link" href="javascript:;" data-report-id="<%= report.id %>" data-action-type="hide">隐藏</a>
		<a class="action-link" href="javascript:;" data-report-id="<%= report.id %>" data-action-type="ignore">忽略</a>
		<% } %>
	</td>
</tr>
<% }); %>