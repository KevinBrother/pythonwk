$(function() {
	$('#top').load('/back/top.html', function() {
		$("#topMenu").click(function() {
			if($("#top").css('height') == '80px') {
				$(this).animate({top: '-16px'});
				$('#topMsg').css('display', 'none');
				$("#top").animate({height: '0px'});
				$("#left").animate({top: '0px'});
				$("#content").animate({top: '0px'});
			} else {
				$(this).animate({top: '64px'});
				$('#topMsg').css('display', 'block');
				$("#top").animate({height: '80px'});
				$("#left").animate({top: '80px'});
				$("#content").animate({top: '80px'});
			}
		});
		
			
		$("#topMenu").hover(function() {
			$(this).css('opacity', 1);
		})
		
		$("#topMenu").mouseleave(function() {
			$(this).css('opacity', 0);
		})
		
	});
	
	
	$('#left').load('/back/left.html', function() {

		$("#menu > li.level1 > a").click(function() {
			$(this).addClass('current').next().show() // 下一个同级元素显示
				.parent().siblings().children("a").removeClass("current") // 父元素的兄弟元素的子元素<a>移除"current"
				.next().hide(); // 它的下一个同级元素隐藏

			console.log($("#menu > li.level1 > a.current > span.current"));
			$("#menu > li.level1 > a > span.current").attr("class", "no-current fa fa-chevron-right fa-lg")
			console.log($(this).find("span[class*=no-current]"))
			$(this).find("span[class*=no-current]").attr("class", "current fa fa-chevron-down fa-lg")

			return false;
		});

		$("ul.level2 a").click(function(e) {
			$("ul.level2 > li > a").removeClass("current");
			$(this).addClass('current');
			$.cookie('pathName', this.href.replace("http://" + location.host, ""), {
				'path': '/'
			});

			location = this.href;

			return false;
		});

		if($.cookie("pathName")) {
			var currMenu = $.find("[href='" + $.cookie("pathName") + "']");
			if(currMenu) {
				$(currMenu).parent().parent().prev().addClass("current");
				$(currMenu).parent().parent().show();
				$(currMenu).addClass("current");

				$("#menu > li.level1 > a > span.current").attr("class", "no-current fa fa-chevron-right fa-lg");
				$(currMenu).parent().parent().prev().find("span[class*='no-current']").attr("class", "current fa fa-chevron-down fa-lg");
			}
		}

		$($.find("[roles]:not([roles*='" + $.cookie("loginName") + "'])")).remove();

		$("#menu > li.level1 > a.current").parent().find('ul.level2').show(); //显示二级菜单

		$("#leftMenu").click(function() {
			if($(this).css('left') == '200px') {
				$(this).animate({left: '0px'});
				$('#left').animate({width: '0px'});
				$("#content").animate({left: 0});
			} else {
				$(this).animate({left: '200px'});
				$('#left').animate({width: '200px'});
				$("#content").animate({left: 200});
			}
		});
		
		$("#leftMenu").hover(function() {
			$(this).css('opacity', 1);
		})
		
		$("#leftMenu").mouseleave(function() {
			$(this).css('opacity', 0);
		})
		
		if(location.pathname == "/back/room/roomState.html") {
			$("#left").css("width", "0px");
			$("#leftMenu").css("left", "0px");
			$("#content").css("left", "10px");
		}
		
	});
	

	if($("#resizable").text() != "") {
		$("#resizable").css("width", $(".body > table.table").width());
		$("#resizable").resizable({
			handles: 'n'
		});
	}
})

// 打印
function preview() { 
	bdhtml=window.document.body.innerHTML; 
	sprnstr="<!--startprint-->"; 
	eprnstr="<!--endprint-->"; 
	prnhtml=bdhtml.substr(bdhtml.indexOf(sprnstr)+17); 
	prnhtml=prnhtml.substring(0,prnhtml.indexOf(eprnstr)); 
	window.document.body.innerHTML=prnhtml; 
	window.print(); 
} 