<div class="create-letter">
	<form class="form-horizontal q-form">
		<div class="form-group">
			<div class="col-xs-2 inline-desc"><span class="required-text">*&nbsp;</span>收信人ID：</div>
			<div class="col-xs-5">
				<input type="text" class="form-control input-sm" name="user_ids">
			</div>
			<div class="col-xs-2">
				<button type="button" class="btn btn-default fileinput-button upload-btn">
					<span>一键上传</span>
					<input id="fileupload" type="file" name="files">
				</button>
			</div>
			<div class="col-xs-3">
				<div class="add-desc">点击按钮可导入Excel文件中的收件人ID。</div>
			</div>
			<div class="col-xs-offset-2 col-xs-5 clear-left">
				<div class="add-desc">支持同时输入多个ID，ID之间请用;(半角英文分号)隔开。例：236626;178787;127719;118899</div>
			</div>
		</div>
		<div class="form-group">
			<div class="col-xs-2 inline-desc"><span class="required-text">*&nbsp;</span>标题：</div>
			<div class="col-xs-5">
				<input type="text" class="form-control input-sm need-count" name="title" maxlength="40">
			</div>
			<div class="col-xs-offset-2 col-xs-5 clear-left">
				<div class="add-desc">当前已输入<span class="current-chars">0</span>个字符, 您还可以输入<span class="remain-chars">40</span>个字符。</div>
			</div>
		</div>
		<div class="form-group">
			<div class="col-xs-2 inline-desc"><span class="required-text">*&nbsp;</span>正文：</div>
			<div class="col-xs-10">
				<textarea id="letterEditor" name="content" class="content-area need-count" maxlength="1000"></textarea>
			</div>
			<div class="col-xs-offset-2 col-xs-5 clear-left">
				<div class="add-desc editor-desc">当前已输入<span class="current-chars">0</span>个字符, 您还可以输入<span class="remain-chars">1000</span>个字符。</div>
			</div>
		</div>
		<div class="form-group">
			<div class="col-xs-2 inline-desc">超链提示：</div>
			<div class="col-xs-2">
				<input type="text" class="form-control input-sm need-count" name="link_remark" maxlength="4">
			</div>
			<div class="col-xs-5">
				<div class="add-desc">当前已输入<span class="current-chars">0</span>个字符, 您还可以输入<span class="remain-chars">4</span>个字符。</div>
			</div>
		</div>
		<div class="form-group inline-desc">
			<div class="col-xs-2">超链地址：</div>
			<div class="col-xs-5">
				<input type="text" class="form-control input-sm" name="outlink">
			</div>
		</div>
		<div class="form-group">
			<div class="col-xs-offset-2 col-xs-10 text-danger hint-block"></div>
			<div class="col-xs-offset-2 col-xs-10 clear-left">
				<button type="button" class="btn btn-default send-btn">发送</button>
				<button type="button" class="btn btn-default cancel-btn">取消</button>
			</div>
		</div>
	</form>
</div>
