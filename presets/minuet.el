(with-eval-after-load 'minuet
  (setq minuet-provider 'openai-compatible)
  (setq minuet-n-completions 1)
  (plist-put minuet-openai-compatible-options :name "Tsubasa")
  (plist-put minuet-openai-compatible-options :model "tsubasa-fast")
  (plist-put minuet-openai-compatible-options :api-key "TSUBASA_API_KEY")
  (plist-put minuet-openai-compatible-options :end-point "https://api.tsubasa.sh/v1/chat/completions")
  (minuet-set-optional-options minuet-openai-compatible-options :max_tokens 256))
