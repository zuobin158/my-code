<div class="h-banner-view">
	<form class="form-horizontal q-form">
		<div class="form-group">
			<div class="inline-desc">Banner名称：</div>
			<div class="col-xs-2">
				<input type="text" class="form-control input-sm" name="bannername">
			</div>
			<div class="inline-desc">是否显示：</div>
			<div class="col-xs-2">
                <select class="form-control input-sm" name="is_active">
                    <option value="">全部</option>
                    <option value="1">是</option>
                    <option value="0">否</option>
                </select>
			</div>

			<div class="col-xs-4">
				<button type="button" class="btn btn-default q-btn">查询</button>
				<button type="button" class="btn btn-default new-btn">新建</button>
			</div>
			<div class="right-block">
				<button type="button" class="btn btn-default order-btn">保存顺序</button>
			</div>
		</div>
		<div class="form-group">
			<div class="text-danger hint-block"></div>
		</div>
	</form>
	<table class="table table-bordered table-xt">
		<thead>
			<tr>
				<th style="width: 9%;">Banner名称</th>
				<th style="width: 9%;">Banner大图</th>
				<th style="width: 9%;">Banner缩略图</th>
				<th style="width: 9%;">背景色/背景URL</th>
				<th style="width: 9%;">背景宽度</th>
				<th style="width: 9%;">图片背景色</th>
				<th style="width: 10%;">链接地址</th>
				<th style="width: 8%;">顺序</th>
				<th style="width: 9%;">创建时间</th>
				<th style="width: 9%;">修改时间</th>
				<th style="width: 9%;">更新人</th>
				<th style="width: 9%;">显示状态</th>
				<th style="width: 10%;">操作</th>
			</tr>
		</thead>
		<tbody class="list-content"></tbody>
	</table>

    <div class="bottom-row">
        <button type="button" class="btn btn-default preview-btn">预览</button>
        <button type="button" class="btn btn-default publish-btn">发布</button>
    </div>
    <div class="preview-panel">

    </div>

	<div class="modal fade create-modal" id="create-modal" tabindex="-1" role="dialog">
		<div class="modal-dialog modal-lg">
			<div class="modal-content">
				<div class="modal-header">
					<h4 class="modal-title">新建Banner</h4>
				</div>
				<div class="modal-body">
					<div class="create-content"></div>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default save-create-btn">保存</button>
					<button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
				</div>
			</div>
		</div>
	</div>
	<div class="modal fade preview-modal" id="preview-modal" tabindex="-1" role="dialog">
		<div class="modal-dialog modal-lg">
			<div class="modal-content">
				<div class="modal-header">
					<h4 class="modal-title">图片预览</h4>
				</div>
				<div class="modal-body">
					<p class="preview-content"></p>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
				</div>
			</div>
		</div>
	</div>
	<div class="modal fade edit-modal" id="edit-modal" tabindex="-1" role="dialog">
		<div class="modal-dialog modal-lg">
			<div class="modal-content">
				<div class="modal-header">
					<h4 class="modal-title">Banner编辑</h4>
				</div>
				<div class="modal-body">
					<div class="edit-content"></div>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default save-edit-btn">保存</button>
					<button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
				</div>
			</div>
		</div>
	</div>
</div>
