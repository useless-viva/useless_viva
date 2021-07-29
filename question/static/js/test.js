// #btn 버튼을 클릭했을 때
$("#btn").click(function () {
    // #result_page의 display가 "none"일 경우 (접혀있는 경우)
    if ($("#result_page").css("display") == "none") {
        // #more 버튼 감추기
        $("#btn").hide();
        $("#btn2").hide();
        // #result_page 보이기
        $("#result_page").show();
    } else {
        // #result_page의 display가 "block"인 경우 (펼쳐져 있는 경우)
        $("#btn").show();
    }
});