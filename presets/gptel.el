;;; gptel.el --- Tsubasa configuration -*- lexical-binding: t; -*-
(with-eval-after-load 'gptel
  (require 'gptel-openai)
  (gptel-make-openai "Tsubasa"
    :host "api.tsubasa.sh"
    :endpoint "/v1/chat/completions"
    :key (lambda () (or (getenv "TSUBASA_API_KEY")
                       (user-error "Set TSUBASA_API_KEY before using Tsubasa")))
    :stream t
    :request-params '(:max_tokens 4096)
    :models '((tsubasa-fast :context-window 32.768 :capabilities nil)
              (tsubasa-pro :context-window 32.768 :capabilities nil))))
