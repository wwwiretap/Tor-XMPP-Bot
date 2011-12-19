<?php

// activate full error reporting
error_reporting(E_ALL & E_STRICT);

include 'XMPPHP/XMPP.php';

#Use XMPPHP_Log::LEVEL_VERBOSE to get more logging for error reports
#If this doesn't work, are you running 64-bit PHP with < 5.2.6?
$conn = new XMPPHP_XMPP('talk.google.com', 5222, 'torbot', 'vum-v0d7xaju', 'xmpphp', 'redteam.io', $printlog=true, $loglevel=XMPPHP_Log::LEVEL_INFO);

$conn->autoSubscribe();

$vcard_request = array();

try {
    $conn->connect();
    while(!$conn->isDisconnected()) {
    	$payloads = $conn->processUntil(array('message', 'presence', 'end_stream', 'session_start', 'vcard'));

    	foreach($payloads as $event) {
    		$pl = $event[1];
                $email_rcv = explode('/', $pl['from']);

                
    		switch($event[0]) {
    			case 'message':

    				print "Message from: {$pl['from']}\n";
    				print $pl['body'] . "\n";
    				print "---------------------------------------------------------------------------------\n";
    				
				$cmd = explode(' ', $pl['body']);
    				
                                switch ($cmd[0]) {
                                    case "test":
                                        echo $response = "I just emailed you a copy to: {$email_rcv[0]}\n";
                                        $conn->message($pl['from'], $body=$response, $type=$pl['type']);
										shell_exec('python /home/architect/dist/lib/torbot/upload.py '. $email_rcv[0]);
                                        break;
                                    default:
                                        echo $response = "Tor XMPP Bot Sample Command: test";
                                        $conn->message($pl['from'], $body=$response, $type=$pl['type']);
                                        break;
                                }								
    			break;
    			case 'presence':
    				print "Presence: {$pl['from']} [{$pl['show']}] {$pl['status']}\n";
    			break;
    			case 'session_start':
    			    print "Session Start\n";   
    			   
			    	$conn->getRoster();
    				$conn->presence($status="Online!");
                	
    			break;
    		}
    	}
    }
} catch(XMPPHP_Exception $e) {
    die($e->getMessage());
}
