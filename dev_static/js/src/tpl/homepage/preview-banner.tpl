<div class="carousel">
	<ul class="carousel_wrap">
		<% _.each(list, function(banner, idx) { %>
		<% if(banner.is_active == 1){ %>
		<li class="carousel_item" data-bg-width="<%= banner.background_image_width %>" data-bg-color="<%= banner.background_image_color %>" data-bg="<%= banner.background %>" data-img="<%= banner.thumbnail %>"><a href="javascript:;" title="<%= banner.name %>" target="_blank"><img src="<%= banner.original %>" /></a></li>
		<% } %>
		<% }); %>
	</ul>
</div>
