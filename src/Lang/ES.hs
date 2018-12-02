module Lang.ES where

lang_space                                        :: String
lang_space  = " "
lang_as,lang_aldred,lang_define,lang_go,lang_jump :: String
lang_print,lang_show,lang_to,lang_value           :: String
lang_as     = "como"
lang_aldred = "alfred"
lang_define = "define"
lang_go     = "vete"
lang_jump   = "salta"
lang_print  = "escribe"
lang_show   = "muestra"
lang_to     = "a"
lang_value  = "el valor de"
lang_bye,lang_moment                              :: String
lang_bye    = "adios" ++ lang_space ++ lang_aldred
lang_moment = lang_define ++ lang_space ++ "el momento"
lang_true,lang_false                              :: [String]
lang_true   = ["verdad", "verdadero", "cierto"]
lang_false  = ["falso", "mentira"]
