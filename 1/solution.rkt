#!/usr/bin/env racket
#lang racket/base
(require racket/file)
(require racket/set)

(define file-path "input")
(define input (file->lines file-path))

; converts a string (including leading +/- to a numerical value)
(define (to-num str)
  (if (eqv? (string-ref str 0) #\-)
    (* -1 (string->number (substring str 1)))
    (string->number (substring str 1))))

(define (sum L)
  (apply + L))

;(display (sum (map to-num input))) (newline)
(define (pop-last lst)
  (car (reverse lst)))

(define (up-to-last lst)
  (reverse (cdr (reverse lst))))

(define (find-all-sums nums starting-value)
  (define (all-sums-tail-call nums starting-value sum-list)
    (if (null? nums)
      (map (lambda (num) (+ starting-value num)) sum-list)
      (all-sums-tail-call (cdr nums) starting-value (append sum-list (list (+ (car nums) (pop-last sum-list)))))))
  (all-sums-tail-call (reverse nums) starting-value '(0)))
      
(define (find-first-pair lst)
  (cond 
    [(null? lst) #f]
    [else 
      (let ([result (find-first-pair (up-to-last lst))])
        (cond 
          [(number? result) result]
          [(member (pop-last lst) (up-to-last lst)) (pop-last lst)]
          [else #f]))]))
        
(define (find-first-repeating-sum nums starting-value sum-history)
  (let ([all-sums (cdr (find-all-sums nums starting-value))])
    (let ([total-history (append sum-history all-sums)])
      (let ([duplicate (find-first-pair total-history)])
        (if (not duplicate)
          (find-first-repeating-sum nums (pop-last total-history) total-history)
          duplicate)))))

; The above solution doesn't work (it takes a long time and uses so much memory it freezes my laptop), but I figured it 
; would be good to try other people's racket solutions since idk anything about racket
; thanks itsnotxhad from reddit
(define (reddit-part-2 nums)
  ; for/fold iterates and initializes accumulators 
  (for/fold ([seen (set)] ; the first accumulator is a set, used for keeping track of all the seen frequencies
             [current-frequency 0] ; the second accumulator is the value of the current frequency
             #:result current-frequency) ; we specify the for/fold loop to return just the frequency, otherwise the 
                                         ; results are all the accumulator values (both the seen set and the current
                                         ; frequency)
            ([num (in-cycle nums)] ; in-cycle iterates through nums and treats it as a infinite cycle, returning to
                                   ; the first element after it reaches the end.
                                   ; this is the 'for-clause', which binds num to the next value in nums 
             #:break (set-member? seen current-frequency)) ; the break clause, which causes this to terminate if 
                                                           ; current-frequency is in the set
    ; this is the body, which needs to return values for each accumulator
    ; so this returns a set, which updates seen with the next frequency, and the next frequency
    ; so we'll break out of this loop when the current frequency has been seen, and return that frequency 
    (let ([next (+ current-frequency num)])
      (values
        (set-add seen current-frequency)
        next))))

(define nums (map to-num input))

;(display (find-all-sums nums 0)) (newline)
;(display (find-first-repeating-sum nums 0 '(0))) (newline)
(display (reddit-part-2 nums)) (newline)
