<ul class="pagination">
	<li class="<%= pages.page==1 ? 'disabled' : '' %>"><a class="first-page" href="javascript:;"><span>&laquo;第1页</span></a></li>
	<li class="<%= pages.page>1 ? '' : 'disabled' %>"><a class="prev-page" href="javascript:;"><span>&lt;上一页</span></a></li>
	<li><span class="page-desc">第<%= pages.page %>页，共<%= pages.totalPage %>页</span></li>
	<li class="<%= pages.page<pages.totalPage ? '' : 'disabled' %>"><a class="next-page" href="javascript:;"><span>下一页&gt;</span></a></li>
	<li class="<%= pages.totalPage==pages.page ? 'disabled' : '' %>"><a class="last-page" href="javascript:;"><span>最后1页&raquo;</span></a></li>
</ul>
<div class="records-control">
	共<%= pages.totalRecord %>条数据，每页显示
	<select class="records-select">
		<option value="10" <%= pages.recordsPerPage == 10 ? "selected" : "" %>>10条</option>
		<option value="20" <%= pages.recordsPerPage == 20 ? "selected" : "" %>>20条</option>
		<option value="50" <%= pages.recordsPerPage == 50 ? "selected" : "" %>>50条</option>
		<option value="100" <%= pages.recordsPerPage == 100 ? "selected" : "" %>>100条</option>
	</select>
</div>