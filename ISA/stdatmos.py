from math import e
def isa(h):
    g0 = 9.80665
    r = 287.
    t0 = 288.15
    p0 = 101325.
    rho0 = 1.225
    h = h

    if h>=0:
        h1 = min(h,11000.)
        t1 = t0 - 0.0065*(h1-0.)
        p1 = (t1/t0)**(-g0/(-0.0065*r))*p0
        rho1 = p1/(r*t1)

        t = t1
        p = p1
        rho = rho1
        c = t - 273.15
        if h>11000.:
            h2 = min(h,20000.)
            t2 = t1
            p2 = (e**(-g0/(r*t2)*(h2-11000.)))*p1
            rho2 = p2/(r*t2)
    
            t = t2
            p = p2
            rho = rho2
            c = t - 273.15
            if h>20000.:
                h3 = min(h,32000.)
                t3 = t2 + 0.001*(h3-20000.)
                p3 = (t3/t2)**(-g0/(0.001*r))*p2
                rho3 = p3/(r*t3)

                t = t3
                p = p3
                rho = rho3
                c = t - 273.15
                if h>32000.:
                    h4 = min(h,47000.)
                    t4 = t3 + 0.0028*(h4-32000.)
                    p4 = (t4/t3)**(-g0/(0.0028*r))*p3
                    rho4 = p4/(r*t4)

                    t = t4
                    p = p4
                    rho = rho4
                    c = t - 273.15
                    if h>47000.:
                        h5 = min(h,51000.)
                        t5 = t4
                        p5 = (e**(-g0/(r*t5)*(h5-47000.)))*p4
                        rho5 = p5/(r*t5)

                        t = t5
                        p = p5
                        rho = rho5
                        c = t - 273.15
                        if h>51000.:
                            h6 = min(h,71000.)
                            t6 = t5 - 0.0028*(h6-51000.)
                            p6 = (t6/t5)**(-g0/(-0.0028*r))*p5
                            rho6 = p6/(r*t6)

                            t = t6
                            p = p6
                            rho = rho6
                            c = t - 273.15
                            if h>71000.:
                                h7 = min(h,86000.)
                                t7 = t6 - 0.0020*(h7-71000.)
                                p7 = (t7/t6)**(-g0/(-0.0020*r))*p6
                                rho7 = p7/(r*t7)

                                t = t7
                                p = p7
                                rho = rho7
                                c = t - 273.15  
    return (t, p, rho)