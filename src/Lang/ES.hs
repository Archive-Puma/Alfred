module Lang.ES where

lang_space                                          :: String
lang_space  = " "
lang_adds,lang_alfred,lang_define,lang_go,lang_jump :: String
lang_mult,lang_print,lang_show,lang_subs,lang_to    :: String
lang_value                                          :: String
lang_adds   = "sumale"
lang_alfred = "alfred"
lang_define = "define"
lang_go     = "vete"
lang_jump   = "salta"
lang_mult   = "multiplica por"
lang_print  = "escribe"
lang_show   = "muestra"
lang_subs   = "restale"
lang_to     = "a"
lang_value  = "el valor de"
lang_as,lang_bye,lang_moment                        :: String
lang_as     = lang_space ++ "como"
lang_bye    = "adios" ++ lang_space ++ lang_alfred
lang_moment = lang_define ++ lang_space ++ "el momento"
lang_true,lang_false                                :: [String]
lang_true   = ["verdadero","verdad","cierto"]
lang_false  = ["falso","mentira"]
