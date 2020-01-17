<?php
/* ========================================================================= *\

  Heigscore 

  Global heighscore list, for coding pirate games

\* ========================================================================= */
$list_max_length = 50;

// Initialize storage
require "rocket-store.php";
$options = [
  "data_storage_area" => realpath("../../data/api")
 ,"data_format"       => RS_FORMAT_JSON
];
$rs = new Paragi\RocketStore($options);

// compare score in list of arrays
function list_cmp($a, $b){
  if ( $a['score'] == $b['score'] ) return 0;
  return ($a['score'] < $b['score']) ? 1 : -1;
}

//Handle request
if($_REQUEST['service'] == 'KDCTY9560F3E3563A6SERWERWEW875EVYVRI' && !empty($_REQUEST['key']) ){
  
  $response = $rs->get("key-store",str_replace('*?','',$_REQUEST['key']));
  $list = $response['result'][$_REQUEST['key']];

  do { 
    if( !empty($_REQUEST['value']) ){
      try{
        $data = json_decode($_REQUEST['value'],true);
        if( !is_array($data)) break;
        if( empty($data['name']) || empty($data['score'] ) ) break;
      } catch (Exception $e) {
        break;
      }
      $list[] = $data;
      usort($list, "list_cmp");
      $list = array_slice ( $list , 0, $list_max_length );
      $response = $rs->post("key-store",$_REQUEST['key'], $list);
    }
  } while(false);
  echo json_encode($list);

} else {
  http_response_code(404);
}

/*
$list = [
  ["name" => "Jesper Sommer", "score" => 1234],
  ["name" => "Henrik", "score" => 1233],
  ["name" => "Martin", "score" => 1232],
  ["name" => "Simon", "score" => 1231],
  ["name" => "Emil", "score" => 34]
];
$rs->post("key-store",$_REQUEST['key'], $list);
*/
?>