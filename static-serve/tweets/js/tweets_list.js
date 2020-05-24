
function loadContainer(tweetContainerID) {

    ///////////////////// variable declarartion part //////////////////////////////
    var charStart = 140;
    var charsCurrent = 0;
    var nextPage = null;
    var tweetContainer; // initially this is undefined
    var initialUrl; // initially this is undefined also
    loadContainer.fetchTweetsAnchor = fetchTweets; // making the fetchtweets equal so we can call it from outside eq: document.ready()
    
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
                        innerdiv.html(newtext)
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
                alert("You can't retweet same tweet in the same day again !");
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

        $("#replyModal").modal({

        });

        // $.ajax({
        //     type: "GET",
        //     url: url,
        //     success: function (response) {
        //         //console.log(response);
        //         attachTweets(response, true);
        //         updateHashLinks();
        //         updateATTLinks();
        //     },
        //     error: function (error) {
        //         //console.log(error.status, error.statusText);
        //         alert("You can't retweet same tweet in the same day again !");
        //     }
        // });
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
        }else{

            $.each(tweetlist, function (index, object) {
                attachTweets(object, false);
            });
        }
        
    }

    function formatTweet(value){

        let verb;
        let preContent;
        let container;
        let isReply;

        isReply = value.isReply;

        console.log(isReply);

        if (value.is_liked_by_user){
            verb = "Dislike";
        }else{
            verb = "Like";  
        }

        console.log(value.is_liked_by_user);

        if (value.parent && !isReply){

            preContent = 
                "<span class='grey-class'>"+
            
                    "Retweet via " + "@" +value.parent.user.username + " on " + value.date_display  +
        
                "</span>" + "<br/><br/>"
                
            // changing the tweet to parent
            // case the rest of the tweet is theirs anyways
            
        } else if (value.parent && isReply){

            preContent = 
            "<span class='grey-class'>"+
        
                "Reply to " + "@" + value.parent.user.username   +
    
            "</span>" + "<br/><br/>" 
        }

        let tweetContent =  
        
            value.content + "<br/>"+
                            
            "via " + "<a href='"+value.user.url+"'>"+ value.user.username +"</a>" +
                
                " | " + value.date_display + " | " +
                
                "<a href='"+ value.tweet_url +"'>View</a>"+
                
                ( initialUrl === "/api/tweet/" ? " | " + "<a class='retweetbtn' href='"+ value.retweet_url +"'>Retweet</a>" : "" ) +

                " | " +
                
                "<a id='" + value.id + "' class='tweetlike' href='#'>" + verb + " ("+ value.likes_count +")</a>" +
    
                " | " +
                
                "<a data-id='"+ value.id +"' data-user='"+ value.user.username +"' class='tweetReply' href='#'>Reply</a>"


        
        if (preContent){
            container = 

                "<div class=\"media\">"+
                    "<div class=\"media-body\">"+

                        preContent +

                        tweetContent +

                    "</div>"+
                "</div>" +
                "<hr>"
        
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

    $(".tweet-form").append("<span id='tweetCharsleft'>"+ charStart +"</span>");

    $(".tweet-form textarea").keyup(function (event) {
        //console.log(event.key, event.keyCode, event.timeStamp);
        var tweetVal = $(this).val();
        charsCurrent = charStart - tweetVal.length;
        var spanText = $("#tweetCharsleft");
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


}

///////////////  Document Body Part //////////////////////////
$(document).ready(function() {
    
    loadContainer();

    // calling nested function from outside the function 
    loadContainer.fetchTweetsAnchor();
});

///////////// END /////////////////////////////////////////////