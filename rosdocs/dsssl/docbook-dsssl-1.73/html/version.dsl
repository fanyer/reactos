;; $Id: version.dsl,v 1.1 2001/10/09 18:50:38 jfilby Exp $
;;
;; This file is part of the Modular DocBook Stylesheet distribution.
;; See ../README or http://www.nwalsh.com/docbook/dsssl/
;;

;; If **ANY** change is made to this file, you _MUST_ alter the
;; following definition:

(define (stylesheet-version)
  (let* ((version "&VERSION;")
	 (verslen (string-length version)))
    (string-append
     "Modular DocBook HTML Stylesheet Version "
     ;; trim off the trailing newline
     (substring version 0 (- verslen 1)))))
