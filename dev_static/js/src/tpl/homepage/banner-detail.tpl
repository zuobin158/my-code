<form class="form-horizontal detail-form">
	<input type="hidden" name="banner_id" value="<%= (typeof id == 'undefined') ? '' : id %>"/>
	<div class="form-group">
		<label class="col-xs-3 control-label">名称：</label>
		<div class="col-xs-9">
			<input type="text" class="form-control" name="name" value="<%= (typeof name == 'undefined') ? '' : name %>"/>
		</div>
	</div>
	<div class="form-group">
		<label class="col-xs-3 control-label"><span class="required-text">*&nbsp;</span>Banner大图URL：</label>
		<div class="col-xs-9">
			<input type="text" class="form-control" name="original" value="<%= (typeof original == 'undefined') ? '' : original %>"/>
		</div>
	</div>
	<div class="form-group">
		<label class="col-xs-3 control-label"><span class="required-text">*&nbsp;</span>Banner缩略图URL：</label>
		<div class="col-xs-9">
			<input type="text" class="form-control" name="thumbnail" value="<%= (typeof thumbnail == 'undefined') ? '' : thumbnail %>"/>
		</div>
	</div>
	<div class="form-group">
		<label class="col-xs-3 control-label">背景色/背景URL：</label>
		<div class="col-xs-9">
			<input type="text" class="form-control" name="background" value="<%= (typeof background == 'undefined') ? '' : background %>"/>
		</div>
	</div>
	<div class="form-group">
		<label class="col-xs-3 control-label">背景宽度：</label>
		<div class="col-xs-9">
			<input type="text" class="form-control" name="background_image_width" value="<%= (typeof background_image_width == 'undefined') ? '' : background_image_width %>"/>
		</div>
	</div>
	<div class="form-group">
		<label class="col-xs-3 control-label">图片背景色：</label>
		<div class="col-xs-9">
			<input type="text" class="form-control" name="background_image_color" value="<%= (typeof background_image_color == 'undefined') ? '' : background_image_color %>"/>
		</div>
	</div>
	<div class="form-group">
		<label class="col-xs-3 control-label"><span class="required-text">*&nbsp;</span>链接地址：</label>
		<div class="col-xs-9">
			<input type="text" class="form-control" name="page_url" value="<%= (typeof page_url == 'undefined') ? '' : page_url %>"/>
		</div>
	</div>
	<div class="form-group">
		<div class="col-xs-9 text-danger hint-block"></div>
	</div>
</form>
