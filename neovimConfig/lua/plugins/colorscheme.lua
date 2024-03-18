return {
  {
    "ray-x/starry.nvim",
    opts = {
      starry_disable_background = true,
    },
  },
  {
    "sainnhe/gruvbox-material",
  },

  {
    "rebelot/kanagawa.nvim",
    opts = {
      transparent = true,
      -- styles = {
      --   sidebars = "transparent",
      --   floats = "transparent",
      -- },
    },
  }, --kanagawa colorscheme
  { "EdenEast/nightfox.nvim" },
  { "rose-pine/neovim", name = "rose-pine" },

  -- Configure LazyVim to load starry
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "gruvbox-material",
    },
  },
}
