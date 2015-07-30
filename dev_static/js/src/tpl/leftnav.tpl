<ul class="nav nav-tabs nav-stacked cms-nav">
	<% _.each(navs, function(nav) { %>
	<% if(nav.child){ %>
	<li>
		<a href="javascript:;" class="nav-header toggle-nav">
			<%= nav.name %><span class="toggle-icon pull-left glyphicon glyphicon-triangle-right"></span>
		</a>
		<ul class="nav nav-list secondmenu collapse">
			<% _.each(nav.child, function(subnav) { %>
			<li>
				<a href="<%= subnav.url %>"><%= subnav.name %></a>
			</li>
			<% }); %>
		</ul>
	</li>
	<% }else{ %>
	<li>
		<a href="<%= nav.url %>"><%= nav.name %></a>
	</li>
	<% } %>
	<% }); %>
</ul>
