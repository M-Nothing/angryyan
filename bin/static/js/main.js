;
var dddd ;
var $, form;
var current_page = 1;
var upload_file = "";
var laypage = "";
function delete_json_row(e){
    $.ajax({
        url		:	"/TT/data/delete",
        data	:	{'del_index':$(e).data('id')-1,},
        dataType	:	'json',
        type	:	'post',
        success	:	function(data){
            if(data && data.respcd =="0000"){
                var dd = data.data;
                $("#desc").val(dd.json_str);
                render_table(dd.data);
            }
        },
        error	:	function(data){
            console.log("Get channel code faild!");
        }
    });

}
function render_table(dd){
    var tbody_html = "";
    var id = 1;
    console.log(dd)
    if(dd.length > 0){
        for(var i=0; i<dd.length; i++)
        {
            tbody_html += "<tr>";
            tbody_html += "<td>" + id + "</td>";
            tbody_html += "<td>" + dd[i]['name'] + "</td>";
            tbody_html += "<td>" + dd[i]['age'] + "</td>";
            tbody_html += "<td><button class='layui-btn layui-btn-radius layui-btn-warm' onclick=delete_json_row(this) data-id='"+id+"'>删除</button></td>";
            tbody_html += "</tr>";
            id += 1;
        }
    }else{
        tbody_html += "<tr><td colspan='4' style='text-align:center;'>暂无数据</td></tr>";
    }
    $("#params_tbody").html(tbody_html);
}


layui.use(['element', 'form', 'laypage', 'layer', 'laydate'], function(){
	form = layui.form;
	laypage = layui.laypage,
	layer = layui.layer,
	$ = layui.jquery;
    var drop_json_file = new Dropzone('#my-form', {
		url: "/TT/sqllog/deal",
		method:"POST",
        addRemoveLinks:true,
        headers : {
            "Accept": "application/json",
            "Cache-Control": "no-cache",
            "X-Requested-With": "XMLHttpRequest"
        },
		autoProcessQueue:false,
        uploadMultiple:false,
        dicRemoveLinks:"x",
        dictCancelUpload: "取消上传",
        dictCancelUploadConfirmation:"是否确定取消上传",
        dictInvalidFileType:"上传文件格式不正确",
        dictFileTooBig:"上传文件过大",
        maxFiles: 1,
        maxFilesize: 20,
        clickable:true,
        acceptedFiles: ".log",
        dictRemoveFile:"删除文件",
        dictMaxFilesExceeded:"只能上传一个文件",
        dictResponseError:"网络异常,请稍后重试...",
        timeout: 800,
        init: function() {
            this.on("addedfile",function(file){
				if(upload_file != ""){
					this.removeFile(upload_file);
				}
				upload_file = file;
				$("#upload_submit").removeClass('layui-btn-disabled');
				$("#upload_submit").attr('disabled',false);
			}),
			this.on("sending", function(file, xhr, data){
				data.append("filetype", file.name.split('.')[1]);
				$("#upload_submit").attr('disabled',false);
				$("#upload_submit").addClass('layui-btn-disabled');
			}),
			this.on("success",function(file, data){
				this.removeFile(file);
				upload_file = "";
				if(typeof(data)==="string"){
					data = JSON.parse(data);
				}
				if(data.respcd == "0000"){
					//layer.msg("<div style='text-align:center;'><i class='layui-icon' style='color:green;font-size:30px;line-height:50px;'>&#xe616; 完成</i></div>",{time:1000, skin:"layui-layer-molv"});
                    dd = data.data.data;

                    var  data_body = '';   
                    console.log(dd);
                    for(var d in dd){
                        for(var x in dd[d]){
                            data_body += '<tr>';
                            data_body += '<td>'+ d +'</td>';
                            data_body += '<td>'+ dd[d][x][0] +'</td>';
                            data_body += '<td>'+ dd[d][x][1] +'</td>';
                            data_body += '</tr>';
                        }
                    }
                    var content = 
                        '<div style="width:500px;" class="m-l-lg">' +
                            '<table class="layui-table m-l-lg">' +
                                '<colgroup>' +
                                    '<col width="150">' +
                                    '<col width="150">' +
                                    '<col width="100">' +
                                '</colgroup>' +
                                '<thead>' + 
                                    '<tr>'+
                                        '<th>Time</th>'+
                                        '<th>sql</th>' + 
                                        '<th>times</th>'+
                                    '</tr>' + 
                                '</thead>' +
                                '<tbody id="params_tbody">' +
                                data_body
                                '</tbody>'+
                            '</table>' +
                        '</div>'

					layer.open({
					  type: 1,
					  area: ['700px', '500px'],
					  title: '文件上传结果',
					  shade: 0.6, 
					  maxmin: false, 
					  anim: 0, 
                      //content: '<div style="text-align:center;margin-top: 60px;"><i class="layui-icon" style="color:green;font-size:20px;line-height:50px;"></i></div>',
                      content: content,
					});
				}else {
					layer.msg("<div style='text-align:left;'><i class='layui-icon' style='color:red;font-size:30px;line-height:50px;'>&#x1006; "+data.respmsg+"</i></div>",{time:10000, skin:"layui-layer-molv"})		
				}
			}),
            this.on("removedfile",function(file){
				upload_file = "";
				$("#upload_submit").attr('disabled', true);
				$("#upload_submit").addClass('layui-btn-disabled');
            })
        }
	});


	$(document).ready(function(){
        function get_json_data(){
            $.ajax({
                url		:	"/TT/data/init",
                data	:	{},
                dataType	:	'json',
                type	:	'get',
                success	:	function(data){
                    if(data && data.respcd =="0000"){
                        var dd = data.data;
                        $("#desc").val(dd.json_str);
                        render_table(dd.data);
                    }
                },
                error	:	function(data){
                    console.log("Get channel code faild!");
                }
            });
        }
        $("#data_upload").click(function(){
            $.ajax({
                url		:	"/TT/data/upload",
                data	:	{'json_data':$("#desc").val(),},
                dataType	:	'json',
                type	:	'post',
                success	:	function(data){
                    if(data && data.respcd =="0000"){
                        var dd = data.data;
                        render_table(dd.data);
                    }
                },
                error	:	function(data){
                    console.log("Get channel code faild!");
                }
            });
        });

		$("#upload_submit").click(function(){
		    drop_json_file.processQueue();	
		});

		$("#upload_reset").click(function(){
			if(upload_file != ''){
				drop_json_file.removeFile(upload_file);
				upload_file == '';
			}
		});
		$("#data_reset").click(function(){
            $("#desc").val('');
		});

		$("#upload_reset").click();
		get_json_data();
	});
});

