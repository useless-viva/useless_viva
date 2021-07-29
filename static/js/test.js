// #btn 버튼을 클릭했을 때
$("#answer-btn1").click(function () {
    var testBox = $('.box');
    testBox.delay(10000).fadeOut()
    // #result_page의 display가 "none"일 경우 (접혀있는 경우)
    if ($("#result_page").css("display") == "none") {
        // 감추기
        $(".num").hide();
        $(".que").hide();
        $(".box").hide();
        $(".box_ddu").hide();
        $("#page_info").hide();
        // #result_page 보이기
        $("#result_page").show();
    }
});