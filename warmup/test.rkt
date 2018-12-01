#!/usr/bin/env racket
#lang racket/base

(define count-args
  (lambda args
    (format "You passed ~a args: ~a" (length args) args)))

(count-args 1 2 3 4 5 6)

(define x '("Apple" "Pear" "Chocolate"))

(define x-map 
  (map (lambda (str)
         (string-append str "  "))
   x))

(for-each display x-map)

; these are comments!!

; file io
(define file "test.txt") 

(define out (open-output-file file #:exists 'append))
(writeln "This is a test file" out)
(close-output-port out)

(require racket/file)
(display (file->string file))

