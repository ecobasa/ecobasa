function calc_position(object, progress_position_pct)
{
  switch(object.type)
  {
    case 'div':
    var progress_duration_px = $(object.contId).width() - $(object.objId).width();
    $(object.objId).css('marginLeft', Math.round(progress_duration_px * progress_position_pct))
    break;
    case 'progressbar':
    $(object.objId).css('width', Math.round(progress_position_pct * 100) + '%');
    $(object.objId).find('span').text(Math.round(progress_position_pct * 100) + '% complete');
    break;
  }       
}

function add_tooltips(blog_posts, contId)
{
  $('[data-toggle="tooltip"]').remove();
  // sort posts by time (reverse)
  blog_posts.sort(function(a,b){
    return a.date.getTime() - b.date.getTime();
  }); 
  
  blog_posts.forEach(function(post){
    var progress_position_pct = (post.date.getTime() - progress_start.getTime()) / (progress_end.getTime() - progress_start.getTime());
    // check boundaries (0 - 100%)
    progress_position_pct = (progress_position_pct > 1.0 || progress_position_pct < 0.0) ? Math.floor(Math.abs(progress_position_pct)) : progress_position_pct;
    var pos = Math.round($(contId).width() * progress_position_pct);
    // check if pos is occupied and move the next one at least a couple of pixels forward
    //console.log(pos);
    if($('a[data-toggle="tooltip"]').length > 0)
    {
      pos = (pos - $('a[data-toggle="tooltip"]:first').position().left < 5) ? $('a[data-toggle="tooltip"]:first').position().left + 7 : pos;
      //console.log('pos: ' + pos + ' / ' + $('a[data-toggle="tooltip"]:first').position().left);
    }
    
    $('<a data-toggle="tooltip" data-placement="top" title="' + post.title + '" style="left:' + pos + 'px"></a>').prependTo(contId).click(function(){
      window.location.href = post.url;
    });
  });
  $('[data-toggle="tooltip"]').tooltip();
};


$(function(){
  $(window).on('resize load', function(){
    var today = new Date();
    var progress_position_pct = (today.getTime() - progress_start.getTime()) / (progress_end.getTime() - progress_start.getTime());
    // check boundaries (0 - 100%)
    progress_position_pct = (progress_position_pct > 1.0 || progress_position_pct < 0.0) ? Math.floor(Math.abs(progress_position_pct)) : progress_position_pct;

    calc_position(
      { objId: '#bus', contId: '#bus-container', type: 'div' },
      progress_position_pct);
    calc_position(
      { objId: '#progress_bar .progress-bar', type: 'progressbar' },
      progress_position_pct);
    add_tooltips(blog_posts, '#progress_bar_wrapper');
  });
});
