return {
  { "rebelot/kanagawa.nvim", opts = { transparent = false } },
  { "comfysage/evergarden", opts = { transparent_background = true, contrast_dark = "hard" } },
  { "rose-pine/neovim", name = "rose-pine" },
  { "sainnhe/gruvbox-material" },
  {
    "catppuccin/nvim",
    opts = {
      transparent_background = false,
      term_colors = true,
    },
  },
  -- Using lazy.nvim
  {
    "cdmill/neomodern.nvim",
    lazy = false,
    priority = 1000,
    config = function()
      require("neomodern").setup({
        -- optional configuration here
      })
      require("neomodern").load()
    end,
  },

  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "kanagawa",
    },
  },
}
