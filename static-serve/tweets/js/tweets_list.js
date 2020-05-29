
function loadContainer(tweetContainerID, fetchOneId) {


    //console.log("FETCHONEID IS: " + fetchOneId);

    ///////////////////// variable declarartion part //////////////////////////////
    var charStart = 140;
    var charsCurrent = 0;
    var nextPage = null;
    var tweetContainer; // initially this is undefined
    var initialUrl; // initially this is undefined also
    //loadContainer.fetchTweetsAnchor = fetchTweets; // making the fetchtweets equal so we can call it from outside eq: document.ready()
    //loadContainer.fetchSingleTweetAnchor = fetchSingleTweet;
    var isSingleTweetDetailPage = false;
    var justASingleReply = false;

    if (tweetContainerID){
        tweetContainer = $("#" + tweetContainerID);
    }else{
        tweetContainer = $("#tweetlist"); // directly saving qjuqry object in the variable declaration part
    }

    initialUrl = tweetContainer.attr("data-url") || "/api/tweet/"; // get data url or initialurl
    
    ////////////////////// END ///////////////////////////////////////////////////

    ///////////////////  Stock Pre Written Functions //////////////////////////////

    function getParameterByName( name ){
        name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
        var regexS = "[\\?&]"+name+"=([^&#]*)";
        var regex = new RegExp( regexS );
        var results = regex.exec( window.location.href );
        if( results == null )
            return "";
        else
            return decodeURIComponent(results[1].replace(/\+/g, " "));
    }

    //////////////////////////  END ///////////////////////////////////////////////

    ///////////////////////// UPDATE LINKS FUNCTIONS ////////////////////////////

    function updateHashLinks(){
        $(".media-body").each(function (index, data) {
        var hashTagRegex = /(^|\s)#([\w\d-]+)/g
        var newText = $(this).html().replace(hashTagRegex, "$1<a href='/tags/$2/'>#$2</a>")
        
        //console.log($(data).text());
        // $(this) and $(data) is interchangable here
        // whenever we need to call a function 
        // on a html element we enclose it with
        // $() in jquery 
        // $(this)   inside a each function
        // means the each returned data itself

        $(data).html(newText); // $(this) is interchangable here


        var innerdiv = $(data).find(".grey-class");

        //console.log("innserdiv is: " + innerdiv.html())
            
        try{
                if (innerdiv){
                        var newtext = innerdiv.html().replace(hashTagRegex, "$1<a href='/tags/$2/'>#$2</a>");
                        innerdiv.html(newtext)
                }
        }
        catch{

        }


        var innerdiv = $(data).find(".nanikore");

        //console.log("innserdiv is: " + innerdiv.html())
            
        try{
                if (innerdiv){
                        var newtext = innerdiv.html().replace(hashTagRegex, "$1<a href='/tags/$2/'>#$2</a>");
                        innerdiv.html(newtext)
                }
        }
        catch{

        }

        });
    }


    function updateATTLinks(){
        $(".media-body").each(function (index, data) {
        var hashTagRegex = /(^|\s)@([\w\d-]+)/g
        var newText = $(this).html().replace(hashTagRegex, "$1<a href='/$2/'>@$2</a>")
        
        //console.log($(data).text());
        // $(this) and $(data) is interchangable here
        // whenever we need to call a function 
        // on a html element we enclose it with
        // $() in jquery 
        // $(this)   inside a each function
        // means the each returned data itself

        $(data).html(newText); // $(this) is interchangable here


        var innerdiv = $(data).find(".grey-class");

        //console.log("innserdiv is: " + innerdiv.html())
            
        try{
                if (innerdiv){
                        var newtext = innerdiv.html().replace(hashTagRegex, "$1<a href='/$2/'>@$2</a>");
                        innerdiv.html(newtext);
                }
        }
        catch{

        }


        var innerdiv = $(data).find(".nanikore");

        //console.log("innserdiv is: " + innerdiv.html())
            
        try{
                if (innerdiv){
                        var newtext = innerdiv.html().replace(hashTagRegex, "$1<a href='/$2/'>@$2</a>");
                        innerdiv.html(newtext)
                }
        }
        catch{

        }

        });
    }


    //////////////////////// END /////////////////////////////////////////////////

    ///////////////////////// Tweet Process and attach part ////////////////////////////


    // this needs to be done because without document.body JQuery 
    // can't track the events on dynamically added objects like Ajax Added Tweets 
    $(document.body).on("click", ".retweetbtn", function (event) {
        event.preventDefault();
        url = $(this).attr("href");

        $.ajax({
            type: "GET",
            url: url,
            success: function (response) {
                //console.log(response);
                attachTweets(response, true);
                updateHashLinks();
                updateATTLinks();
            },
            error: function (error) {
                //console.log(error.status, error.statusText);
                alert("You can't retweet same tweet again !");
            }
        });
    });



    // tweet like toggle
    $(document.body).on("click", ".tweetlike", function (event) {
        event.preventDefault();

        //console.log("HERE IN TWEET LIKE");

        let parentThis = $(this); 
        
        let tweetId = $(this).attr("id");

        if (tweetId){
            url = "/api/tweet/"+tweetId+"/like",
            
            $.ajax({
                type: "GET",
                url: url,
                success: function (response) {
                    
                    if (response.is_liked){
                        parentThis.text("Dislike" + " ("+ response.count +")");
                    }else{
                        parentThis.text("Like" + " ("+ response.count +")");
                    }
    
                },
                error: function (error) {
                    console.log(error.status, error.statusText);
                }
            });
        
        }

    });



    $(document.body).on("click", ".tweetReply", function (event) {
        event.preventDefault();
        data_id = $(this).attr("data-id");
        data_user = $(this).attr("data-user");
        data_content = $(this).parent().find("span.content").text();

        $("#replyModal").modal({
            
        });

        $("#replyModal textarea").after("<input type='hidden' value='" + data_id + "' name='parent_id' />");
        $("#replyModal textarea").after("<input type='hidden' value=" + true + " name='isReply' />");

        $("#replyModal textarea").val("@" + data_user + " ");

        $("#replyModal #replyModalLabel").text("Reply to : " + data_content);

        $("#replyModal").on("shown.bs.modal", function () {
            $("#tweetReplyArea").focus();
        })

        $.ajax({
            type: "GET",
            url: url,
            success: function (response) {
                //console.log(response);
                attachTweets(response, true);
                updateHashLinks();
                updateATTLinks();
            },
            error: function (error) {
                //console.log(error.status, error.statusText);
                alert("You can't retweet same tweet in the same day again !");
            }
        });
    });



    function fetchTweets(url) {

        var requestUrl;

        if (!url){
            requestUrl = initialUrl;
        }else{
            requestUrl = url;
        }

        query = getParameterByName("q");
        console.log(query);

        $.ajax({
            url: requestUrl,
            data: {
                "q": query
            },

            method: "GET",

            success: function(data) {
                nextPage = data.next;

                if (nextPage == null){
                    $(".load-more").css("display", "none");
                }
                parseTweets(data.results)
                updateHashLinks();
                updateATTLinks();
            },

            error: function (data) {
                console.log("ERROR");
                console.log(data);
            }
        });

    }


    function parseTweets(tweetlist) {

        if (tweetlist == 0){
            tweetContainer.text("No Tweets Found");
        }
        else if(tweetlist == 1){
            justASingleReply = true;
        }else{

            $.each(tweetlist, function (index, object) {
                if (!object.isReply && isSingleTweetDetailPage){
                    //console.log("OLAAAAAAAAAAAAAAAAAA");
                    attachTweets(object, true);

                }else{
                    attachTweets(object, false);
                }
            
            });
        }

        justASingleReply = false;
        
    }

    function formatTweet(value){

        let verb;
        let preContent;
        let container;
        let isReply;

////////////////////////////////////////////////////////////////////////////////////////////////////////////

        console.log("isSingleTweetDetailPage: " + isSingleTweetDetailPage);

///////////////////////////////////////////////////////////////////////////////////////////////////////////


        isReply = value.isReply;

        let replyId = value.id 

        //console.log(isReply);

        if (value.is_liked_by_user){
            verb = "Dislike";
        }else{
            verb = "Like";  
        }

        //console.log(value.is_liked_by_user);

        if (value.parent && !isReply){

            preContent = 
                "<span class='grey-class'>"+
            
                    "Retweet via " + "@" +value.parent.user.username + " on " + value.date_display  + 
                    "<br><br>" +
                    value.parent.content +
        
                "</span>" + "<br/><br/>"
                
            // changing the tweet to parent
            // case the rest of the tweet is theirs anyways
            
        } else if (value.parent && isReply){

            replyId = value.parent.id 

            preContent = 
            "<span class='grey-class'>"+
        
                "Reply to " + "@" + value.parent.user.username   + 
                "<br><br>" +
                value.parent.content +
    
            "</span>" + "<br/><br/>" 
        }

        let tweetContent =  
            "<span class='content'>"+
                value.content +
            "</span>" + "<br/>"+
                            
            "via " + "<a href='"+value.user.url+"'>"+ value.user.username +"</a>" +
                
                " | " + value.date_display + " | " +
                
                "<a href='"+ value.tweet_url +"'>View</a>"+
                
                ( initialUrl === "/api/tweet/" ? " | " + "<a class='retweetbtn' href='"+ value.retweet_url +"'>Retweet</a>" : "" ) +

                " | " +
                
                "<a id='" + value.id + "' class='tweetlike' href='#'>" + verb + " ("+ value.likes_count +")</a>" +
    
                " | " +
                
                "<a data-id='"+ replyId +"' data-user='"+ value.user.username +"' class='tweetReply' href='#'>Reply</a>"


        
        if (preContent){
            container = 

                "<div class=\"media\">"+
                    "<div class=\"media-body\">"+

                        preContent +

                        tweetContent +

                    "</div>"+
                "</div>" +
                "<hr>"

            if (isReply && isSingleTweetDetailPage && !justASingleReply){

                container = 

                "<div class=\"media\" style='margin-left: 100px;'>"+
                    "<div class=\"media-body\">"+

                        preContent +

                        tweetContent +

                    "</div>"+
                "</div>" +
                "<hr>"
            }
        
        } else{
            container = 
            
                "<div class=\"media\">"+
                    "<div class=\"media-body\">"+

                        tweetContent +

                    "</div>"+
                "</div>" +
                "<hr>"
        }

        
        return container;
                            

    }

    function attachTweets(value, prepend) {

        let formattedHtml = formatTweet(value);

        if (prepend === true){
            tweetContainer.prepend(formattedHtml);
        }
        else{
            tweetContainer.append(formattedHtml);
        }
        
    }

    //////////////////////////////  END ////////////////////////////////////////////

    //////////////////////////  Ajax Tweet Part ////////////////////////////////

    $(".tweet-form").submit(function(event){

        console.log("TWEETFORM!!!!!!!!");

        // prevents a form's default sunmit function
        event.preventDefault();

        var thisForm = $(this);
        var FormData = thisForm.serialize();

        if (charsCurrent >= 0){

            $.ajax({
                url: "/api/tweet/create/",
                data: FormData,
                method: "POST",

                success: function(data) {
                    thisForm.find("input[type=text], textarea").val("");
                    attachTweets(data, true);
                    updateHashLinks();
                    updateATTLinks();
                    $("#replyModal").modal("hide");
                },

                error: function(data) {
                    console.log("ERROR");
                    console.log(data.status);
                    console.log(data.statusText);
                }
            });

        }else{
            alert("Tweet Too long type something shorter");
        }

    });

    ////////////////////// END ///////////////////////////////////////////////

    ////////////////////////// Character limit part ////////////////////////////////////////////

    $(".tweet-form").append("<span class='tweetCharsleft' style='margin-left: 20px;'>"+ charStart +"</span>");

    $(".tweet-form textarea").keyup(function (event) {
        //console.log(event.key, event.keyCode, event.timeStamp);
        var tweetVal = $(this).val();
        charsCurrent = charStart - tweetVal.length;
        var spanText = $(this).parent().parent().parent().find(".tweetCharsleft");
        spanText.text(charsCurrent);
        
        if (charsCurrent === 0){
            spanText.removeClass("red-class");
            spanText.removeClass("green-class");
            spanText.addClass("grey-class");
        }
        else if (charsCurrent > 0){
            spanText.removeClass("red-class");
            spanText.removeClass("grey-class");
            spanText.addClass("green-class");
        } else if (charsCurrent < 0){
            spanText.removeClass("grey-class");
            spanText.removeClass("green-class");
            spanText.addClass("red-class");
        }
    });

    /////////////////////////// END /////////////////////////////////////////////////

    ////////////////////////// Load More Part /////////////////////////////////////


    $(".load-more").bind("click", function (event) {
    event.preventDefault();
    if (nextPage){
        fetchTweets(nextPage);
    }


    });


    ///////////////////////////// END /////////////////////////////////////////////


    /////////////////////////// FETCH SINGLE TWEET////////////////////////////////



    function fetchSingleTweet(fetchOneId) {

        var fetchUrl = "/api/tweet/" + fetchOneId + "/";

        isSingleTweetDetailPage = true;

        console.log(fetchOneId);

        //var requestUrl;

        // if (!url){
        //     requestUrl = initialUrl;
        // }else{
        //     requestUrl = url;
        // }

        query = getParameterByName("q");
        console.log(query);

        $.ajax({
            url: fetchUrl,
             data: {
                 "q": query
             },

            method: "GET",

            success: function(data) {
                nextPage = data.next;

                if (nextPage == null){
                    $(".load-more").css("display", "none");
                 }
                 parseTweets(data.results)
                 updateHashLinks();
                 updateATTLinks();

                 isSingleTweetDetailPage = false;
            },

            error: function (data) {
                console.log("ERROR");
                console.log(data);

                isSingleTweetDetailPage = false;
            }
        });

    }


    /////////////////////////// END //////////////////////////////////////////////
    //console.log("Reached the end");
    if(fetchOneId){

        //console.log("IN SINGLE TWEET");
        fetchSingleTweet(fetchOneId);
    }else{
        fetchTweets();
    }

}

